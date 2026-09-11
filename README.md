# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 397
- HTTP: 94 alive / 65 gold
- HTTPS: 33 alive / 18 gold
- SOCKS4: 162 alive / 142 gold
- SOCKS5: 192 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48780
- Ever gold: 1566

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
