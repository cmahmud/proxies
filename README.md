# SyndProxy validated proxy pool

## Current pool

- Alive now: 580
- Gold now: 451
- HTTP: 97 alive / 77 gold
- HTTPS: 111 alive / 32 gold
- SOCKS4: 179 alive / 164 gold
- SOCKS5: 193 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47426
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
