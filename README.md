# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 404
- HTTP: 89 alive / 59 gold
- HTTPS: 92 alive / 21 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 173 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42970
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
