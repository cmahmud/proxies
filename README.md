# SyndProxy private pool

## Current pool

- Alive now: 834
- Gold now: 384
- HTTP: 255 alive / 86 gold
- HTTPS: 200 alive / 26 gold
- SOCKS4: 183 alive / 128 gold
- SOCKS5: 196 alive / 144 gold

## Historical pool

- Discovered: 161996
- Ever alive: 31350
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
