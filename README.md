# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 461
- HTTP: 135 alive / 93 gold
- HTTPS: 63 alive / 35 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 189 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49376
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
