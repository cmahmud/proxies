# SyndProxy private pool

## Current pool

- Alive now: 1031
- Gold now: 398
- HTTP: 321 alive / 87 gold
- HTTPS: 220 alive / 25 gold
- SOCKS4: 237 alive / 137 gold
- SOCKS5: 253 alive / 149 gold

## Historical pool

- Discovered: 164246
- Ever alive: 32097
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
