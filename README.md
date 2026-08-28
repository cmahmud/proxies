# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 402
- HTTP: 82 alive / 58 gold
- HTTPS: 78 alive / 20 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 173 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42927
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
