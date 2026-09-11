# SyndProxy validated proxy pool

## Current pool

- Alive now: 460
- Gold now: 378
- HTTP: 84 alive / 65 gold
- HTTPS: 42 alive / 22 gold
- SOCKS4: 149 alive / 121 gold
- SOCKS5: 185 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48736
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
