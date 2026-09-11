# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 359
- HTTP: 109 alive / 77 gold
- HTTPS: 75 alive / 29 gold
- SOCKS4: 231 alive / 73 gold
- SOCKS5: 234 alive / 180 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48580
- Ever gold: 1548

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
