# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 407
- HTTP: 110 alive / 77 gold
- HTTPS: 63 alive / 18 gold
- SOCKS4: 172 alive / 153 gold
- SOCKS5: 180 alive / 159 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48092
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
