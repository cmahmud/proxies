# SyndProxy validated proxy pool

## Current pool

- Alive now: 616
- Gold now: 473
- HTTP: 134 alive / 96 gold
- HTTPS: 112 alive / 41 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 199 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45042
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
