# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 384
- HTTP: 87 alive / 66 gold
- HTTPS: 43 alive / 21 gold
- SOCKS4: 157 alive / 125 gold
- SOCKS5: 191 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48742
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
