# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 414
- HTTP: 121 alive / 85 gold
- HTTPS: 72 alive / 24 gold
- SOCKS4: 172 alive / 146 gold
- SOCKS5: 182 alive / 159 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48053
- Ever gold: 1516

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
