# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 428
- HTTP: 104 alive / 73 gold
- HTTPS: 36 alive / 18 gold
- SOCKS4: 184 alive / 164 gold
- SOCKS5: 189 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48929
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
