# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 368
- HTTP: 94 alive / 45 gold
- HTTPS: 40 alive / 10 gold
- SOCKS4: 182 alive / 155 gold
- SOCKS5: 207 alive / 158 gold

## Historical pool

- Discovered: 173050
- Ever alive: 32993
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
