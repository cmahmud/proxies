# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 397
- HTTP: 94 alive / 68 gold
- HTTPS: 42 alive / 21 gold
- SOCKS4: 161 alive / 135 gold
- SOCKS5: 191 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48766
- Ever gold: 1566

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
