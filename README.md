# SyndProxy validated proxy pool

## Current pool

- Alive now: 470
- Gold now: 370
- HTTP: 75 alive / 44 gold
- HTTPS: 40 alive / 10 gold
- SOCKS4: 173 alive / 156 gold
- SOCKS5: 182 alive / 160 gold

## Historical pool

- Discovered: 173068
- Ever alive: 33008
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
