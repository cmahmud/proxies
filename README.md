# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 463
- HTTP: 130 alive / 94 gold
- HTTPS: 60 alive / 35 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 187 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49375
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
