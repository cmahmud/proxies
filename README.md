# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 429
- HTTP: 106 alive / 73 gold
- HTTPS: 37 alive / 19 gold
- SOCKS4: 184 alive / 164 gold
- SOCKS5: 191 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48929
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
