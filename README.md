# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 392
- HTTP: 92 alive / 58 gold
- HTTPS: 36 alive / 13 gold
- SOCKS4: 173 alive / 158 gold
- SOCKS5: 190 alive / 163 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33342
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
