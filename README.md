# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 467
- HTTP: 121 alive / 93 gold
- HTTPS: 61 alive / 38 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 191 alive / 176 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49380
- Ever gold: 1579

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
