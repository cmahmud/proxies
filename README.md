# SyndProxy private pool

## Current pool

- Alive now: 816
- Gold now: 398
- HTTP: 242 alive / 90 gold
- HTTPS: 126 alive / 20 gold
- SOCKS4: 216 alive / 151 gold
- SOCKS5: 232 alive / 137 gold

## Historical pool

- Discovered: 155695
- Ever alive: 29242
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
