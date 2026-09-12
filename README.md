# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 467
- HTTP: 116 alive / 92 gold
- HTTPS: 51 alive / 37 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 190 alive / 176 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49399
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
