# SyndProxy private pool

## Current pool

- Alive now: 758
- Gold now: 389
- HTTP: 186 alive / 86 gold
- HTTPS: 141 alive / 24 gold
- SOCKS4: 214 alive / 128 gold
- SOCKS5: 217 alive / 151 gold

## Historical pool

- Discovered: 151059
- Ever alive: 27300
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
