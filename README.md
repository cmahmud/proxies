# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 441
- HTTP: 105 alive / 82 gold
- HTTPS: 50 alive / 27 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 182 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49202
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
