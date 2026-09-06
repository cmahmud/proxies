# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 407
- HTTP: 109 alive / 82 gold
- HTTPS: 62 alive / 22 gold
- SOCKS4: 160 alive / 146 gold
- SOCKS5: 183 alive / 157 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48053
- Ever gold: 1516

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
