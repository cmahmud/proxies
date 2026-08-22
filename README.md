# SyndProxy private pool

## Current pool

- Alive now: 984
- Gold now: 402
- HTTP: 318 alive / 92 gold
- HTTPS: 209 alive / 25 gold
- SOCKS4: 210 alive / 136 gold
- SOCKS5: 247 alive / 149 gold

## Historical pool

- Discovered: 164246
- Ever alive: 32103
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
