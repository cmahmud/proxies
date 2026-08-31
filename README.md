# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 422
- HTTP: 90 alive / 59 gold
- HTTPS: 66 alive / 30 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 191 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45498
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
