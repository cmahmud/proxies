# SyndProxy validated proxy pool

## Current pool

- Alive now: 584
- Gold now: 431
- HTTP: 103 alive / 79 gold
- HTTPS: 120 alive / 23 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 190 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42454
- Ever gold: 1357

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
