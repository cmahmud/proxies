# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 468
- HTTP: 119 alive / 93 gold
- HTTPS: 53 alive / 37 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 189 alive / 176 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49400
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
