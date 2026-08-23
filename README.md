# SyndProxy validated proxy pool

## Current pool

- Alive now: 473
- Gold now: 365
- HTTP: 91 alive / 53 gold
- HTTPS: 41 alive / 11 gold
- SOCKS4: 165 alive / 151 gold
- SOCKS5: 176 alive / 150 gold

## Historical pool

- Discovered: 174123
- Ever alive: 33057
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
