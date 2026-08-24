# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 384
- HTTP: 88 alive / 53 gold
- HTTPS: 53 alive / 12 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 181 alive / 161 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33494
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
