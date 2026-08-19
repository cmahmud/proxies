# SyndProxy private pool

## Current pool

- Alive now: 1272
- Gold now: 538
- HTTP: 470 alive / 182 gold
- HTTPS: 339 alive / 59 gold
- SOCKS4: 219 alive / 142 gold
- SOCKS5: 244 alive / 155 gold

## Historical pool

- Discovered: 125594
- Ever alive: 19574
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
