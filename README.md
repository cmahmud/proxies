# SyndProxy validated proxy pool

## Current pool

- Alive now: 469
- Gold now: 378
- HTTP: 90 alive / 65 gold
- HTTPS: 43 alive / 24 gold
- SOCKS4: 147 alive / 119 gold
- SOCKS5: 189 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48732
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
