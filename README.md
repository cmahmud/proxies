# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 393
- HTTP: 88 alive / 62 gold
- HTTPS: 38 alive / 15 gold
- SOCKS4: 186 alive / 155 gold
- SOCKS5: 185 alive / 161 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48147
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
