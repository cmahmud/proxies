# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 456
- HTTP: 116 alive / 84 gold
- HTTPS: 52 alive / 33 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 192 alive / 177 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49226
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
