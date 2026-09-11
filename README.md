# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 424
- HTTP: 107 alive / 74 gold
- HTTPS: 34 alive / 18 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 181 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48975
- Ever gold: 1569

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
