# SyndProxy validated proxy pool

## Current pool

- Alive now: 636
- Gold now: 384
- HTTP: 128 alive / 67 gold
- HTTPS: 173 alive / 22 gold
- SOCKS4: 159 alive / 145 gold
- SOCKS5: 176 alive / 150 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39854
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
