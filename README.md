# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 424
- HTTP: 103 alive / 73 gold
- HTTPS: 61 alive / 23 gold
- SOCKS4: 183 alive / 166 gold
- SOCKS5: 179 alive / 162 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49023
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
