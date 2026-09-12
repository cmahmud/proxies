# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 434
- HTTP: 111 alive / 85 gold
- HTTPS: 52 alive / 28 gold
- SOCKS4: 170 alive / 156 gold
- SOCKS5: 186 alive / 165 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49428
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
