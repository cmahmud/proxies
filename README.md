# SyndProxy private pool

## Current pool

- Alive now: 1243
- Gold now: 566
- HTTP: 456 alive / 193 gold
- HTTPS: 317 alive / 95 gold
- SOCKS4: 251 alive / 145 gold
- SOCKS5: 219 alive / 133 gold

## Historical pool

- Discovered: 136255
- Ever alive: 22876
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
