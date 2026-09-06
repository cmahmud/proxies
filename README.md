# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 408
- HTTP: 109 alive / 78 gold
- HTTPS: 62 alive / 19 gold
- SOCKS4: 173 alive / 152 gold
- SOCKS5: 179 alive / 159 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48092
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
