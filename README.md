# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 384
- HTTP: 128 alive / 53 gold
- HTTPS: 40 alive / 11 gold
- SOCKS4: 173 alive / 158 gold
- SOCKS5: 182 alive / 162 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33453
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
