# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 444
- HTTP: 89 alive / 77 gold
- HTTPS: 92 alive / 31 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 188 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47350
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
