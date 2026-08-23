# SyndProxy validated proxy pool

## Current pool

- Alive now: 466
- Gold now: 380
- HTTP: 80 alive / 52 gold
- HTTPS: 47 alive / 13 gold
- SOCKS4: 164 alive / 155 gold
- SOCKS5: 175 alive / 160 gold

## Historical pool

- Discovered: 175243
- Ever alive: 33123
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
