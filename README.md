# SyndProxy validated proxy pool

## Current pool

- Alive now: 613
- Gold now: 474
- HTTP: 129 alive / 99 gold
- HTTPS: 117 alive / 39 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 198 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45042
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
