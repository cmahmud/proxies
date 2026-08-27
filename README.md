# SyndProxy validated proxy pool

## Current pool

- Alive now: 644
- Gold now: 405
- HTTP: 123 alive / 63 gold
- HTTPS: 161 alive / 12 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 189 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40866
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
