# SyndProxy private pool

## Current pool

- Alive now: 1094
- Gold now: 417
- HTTP: 353 alive / 93 gold
- HTTPS: 242 alive / 20 gold
- SOCKS4: 228 alive / 143 gold
- SOCKS5: 271 alive / 161 gold

## Historical pool

- Discovered: 136195
- Ever alive: 22307
- Ever gold: 896

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
