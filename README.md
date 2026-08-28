# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 428
- HTTP: 100 alive / 77 gold
- HTTPS: 113 alive / 22 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 190 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42454
- Ever gold: 1357

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
