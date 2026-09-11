# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 389
- HTTP: 93 alive / 64 gold
- HTTPS: 37 alive / 17 gold
- SOCKS4: 153 alive / 140 gold
- SOCKS5: 195 alive / 168 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48775
- Ever gold: 1566

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
