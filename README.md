# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 446
- HTTP: 118 alive / 83 gold
- HTTPS: 72 alive / 31 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 199 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44591
- Ever gold: 1407

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
