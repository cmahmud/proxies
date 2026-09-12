# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 466
- HTTP: 125 alive / 93 gold
- HTTPS: 64 alive / 37 gold
- SOCKS4: 182 alive / 161 gold
- SOCKS5: 189 alive / 175 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49379
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
