# SyndProxy private pool

## Current pool

- Alive now: 883
- Gold now: 396
- HTTP: 267 alive / 91 gold
- HTTPS: 181 alive / 15 gold
- SOCKS4: 237 alive / 155 gold
- SOCKS5: 198 alive / 135 gold

## Historical pool

- Discovered: 119829
- Ever alive: 18262
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
