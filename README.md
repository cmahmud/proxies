# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 408
- HTTP: 92 alive / 64 gold
- HTTPS: 105 alive / 18 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 186 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41440
- Ever gold: 1331

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
