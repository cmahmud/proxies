# SyndProxy validated proxy pool

## Current pool

- Alive now: 617
- Gold now: 425
- HTTP: 156 alive / 76 gold
- HTTPS: 90 alive / 23 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 197 alive / 164 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33887
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
